use strict;
use warnings;
use utf8;
use open IN  => ":utf8";
use open OUT => ":utf8";
use open IO => ":utf8";

package IssuesTemplate;

my $dir = './md';

sub list {
  chdir("$dir");
  my @mdfiles;

  # ディレクトリ内のmarkdownファイル名を取得
  @mdfiles = glob "*.md";
  
  return \@mdfiles;
}


sub get {
  my $filename = shift;
  #my $filepath = $dir .'/'. chomp($filename);
  chdir("$dir");
  my $filepath = $filename;
  my $body;
  
  open(IN, $filepath);
  while (my $line = <IN>) {
    $body .= $line;
  }
  
  return \$body;
}

1;
