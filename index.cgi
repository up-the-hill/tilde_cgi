#!/usr/bin/perl

use strict;
use warnings;

# File to store the visit count
my $counter_file = "counter.txt";
my $messages_file = "messages.txt";

# Read the current visit count, up by 1, and write to file
my $visits = read_counter();
$visits++;
update_counter($visits);

# Read the messages from the file
my @messages = read_messages();
my $message_list = make_message_list(@messages);

sub read_counter {
    if (-e $counter_file) {
        open(my $fh, "<", $counter_file) or die "Cannot open file $counter_file: $!";
        my $visits = <$fh>;
        close($fh);
        return $visits;
    } else {
        return 0;
    }
}

sub read_messages {
    if (-e $messages_file) {
        open(my $fh, "<", $messages_file) or die "Cannot open file $messages_file $!";
        my @messages = <$fh>;
        close($fh);
        return @messages;
    } else {
        return 0;
    }
}

# Function to update the visit count in the file
sub update_counter {
    my ($visits) = @_;
    open(my $fh, ">", $counter_file) or die "Cannot open file $counter_file: $!";
    print $fh $visits;
    close($fh);
}

sub make_message_list {
    my (@messages) = @_;
    my $res = "";
    foreach (@messages) {
        $res = $res . "<li>$_\n"
    }
    return $res
}


print <<HTML_HEADERS;
Status: 200
Content-Type: text/html

HTML_HEADERS

# print the html page
print <<HTML_PAGE;
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Troubadour's online home">
  <link rel="stylesheet" href="./style.css">
  <title>Troubadour</title>
</head>

<body>
  <h1>~~~my online corner~~~</h1>
  <p>Check out my <a href="https://status.cafe/users/troubadour">status.cafe</a></p>

  <p>Feel free to leave me a message here!</p>
  <div class="advisory">
    <h2>messages:</h2>
    <ul class="messages">$message_list</ul>

    <form action="https://tilde.club/~troubadour/add.cgi" method="post">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" required>
      <br>
      <label for="message">Message:</label>
      <input type="text" id="message" name="message" required>
      <input type="submit" value="send!">
    </form>
  </div>
  <p>This website has been visited <b>$visits</b> times!</p>

  <hr>

  <h4>about</h4>

  <p class="info">
    This website was made using cgi (perl)!! it's pretty cool check it out here: <a
      href="https://tilde.club/wiki/cgi.html#introduction">CGI: Making web applications like it’s 90s</a>
  </p>

  <hr>

  <!-- Begin Tilde Club Badge -->
  <center>
    <p><a href="https://tilde.club"><img src="https://tilde.club/~zarate/tildeclub.gif" border="0" width="88"
          height="31" alt="Tilde Club Badge"></a></p>
  </center>
  <!-- End Tilde Club Badge -->

</body>

</html>
HTML_PAGE
