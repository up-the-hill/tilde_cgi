#!/usr/bin/perl

use strict;
use warnings;

use URI::Escape;

my $messages_file = "messages.txt";
my $input = $ENV{CONTENT_TYPE};

my $FormData = '';
read(STDIN, $FormData, $ENV{'CONTENT_LENGTH'});

write_message(sanitize_input(uri_unescape(substr($FormData, 8)) . "\n"));

sub sanitize_input {
    my ($string) = @_;
    $string =~ s/[<>]//g;
    $string =~ tr/+/ /;
    return $string;
}

sub write_message {
    my ($message) = @_;
    open(my $fh, ">>", $messages_file) or die "Cannot open file $messages_file: $!";
    print $fh $message;
    close($fh);
}

print <<HTML_HEADERS;
Status: 301
Location: https://tilde.club/~troubadour/

HTML_HEADERS


