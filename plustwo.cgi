#!/usr/bin/perl

use warnings;
use strict;

my $plustwos_file = "plustwos.txt";

sub plustwo {
  #read the current count
  open(my $fh, "<", $plustwos_file) or die "Cannot open file $plustwos_file $!";
  my $count = <$fh>;
  chomp($count); 
  close($fh);

  #increment by 1
  $count++;

  #store new value
  open(my $fh1, ">", $plustwos_file) or die "Cannot open file $plustwos_file $!";
  print $fh1 $count;
  close($fh1);
}

plustwo();

print <<HTML_HEADERS;
Status: 301
Location: https://tilde.club/~troubadour/

HTML_HEADERS

