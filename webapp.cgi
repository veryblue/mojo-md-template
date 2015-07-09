#!/usr/bin/env perl
use FindBin;
use lib "$FindBin::Bin/../../perl5/lib/perl5";
use lib "./lib";

use Mojolicious::Lite;
use URI::Escape;
use IssuesTemplate;

get '/' => sub {
  my $self = shift;
  my $files = IssuesTemplate::list();
  $self->stash(files => $files);
  $self->render('index');
};

# /file?md=hoge.md
get '/file' => sub {
  my $self = shift;
  my $file = $self->param('md');
  my $md = IssuesTemplate::get($file);
  my $url_md = uri_escape_utf8($$md);
  $self->stash(url_md => $url_md);
  $self->stash(md => $md);
  $self->render('file');
};

get '/uri_escape' => sub {
  my $self = shift;

  $self->render(text => uri_escape_utf8('#'));
};

app->start;
__DATA__

@@ index.html.ep
% layout 'default';
% title 'issue templates';
<h1>issue templates</h1>

<ul>
% for my $file (@$files) {
  <li><a href="file?md=<%= $file %>"><%= $file %></a></li>
% }
</ul>

@@ file.html.ep
% layout 'default';
% title 'templates';
<h1>templates</h1>

<div style="background: #f5f5f5; padding: 1.5em;">
% my $text = $$md;
% $text =~ s/\n/<br>/g;
%== $text
</div>

% my $ibody = $url_md;
<a href="https://github.com/veryblue/test/issues/new?title=test&body=<%= $ibody %>" target="_blank">
create new issue
</a>

@@ layouts/default.html.ep
<!DOCTYPE html>
<html>
  <head><title><%= title %></title></head>
  <body><%= content %></body>
</html>


