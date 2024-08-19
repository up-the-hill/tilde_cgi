#!/usr/bin/perl

use strict;
use warnings;

use URI::Escape;

my $messages_file = "messages.txt";
my $input = $ENV{CONTENT_TYPE};

my $FormData = '';
read(STDIN, $FormData, $ENV{'CONTENT_LENGTH'});

# Parse the incoming form data
my ($name, $message) = parse_form_data($FormData);

# Sanitize both fields
$name = sanitize_input($name);
$message = sanitize_input($message);

write_message("$name: $message\n");


#remove all < and >, and replace + with a space
sub sanitize_input {
    my ($string) = @_;
    $string =~ s/[<>]//g;
    $string =~ tr/+/ /;
    return $string;
}

sub write_message {
    my ($message) = @_;
    if ($message ne "") {
        open(my $fh, ">>", $messages_file) or die "Cannot open file $messages_file: $!";
        print $fh $message;
        close($fh);
    }
}

sub parse_form_data {
    my ($data) = @_;
    # Split the data into key-value pairs
    my %params = map { split(/=/, $_, 2) } split(/&/, $data);
    # Decode the values
    my $name = uri_unescape($params{'name'} // '');
    my $message = uri_unescape($params{'message'} // '');
    return ($name, $message);
}

print <<HTML_HEADERS;
Status: 301
Location: https://tilde.club/~troubadour/

HTML_HEADERS


