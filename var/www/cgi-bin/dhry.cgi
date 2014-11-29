#! /usr/bin/perl
use CGI qw/:standard/;
$times = param('times');
print header, start_html("Result");
print(h1("Result"));
die("could not execute benchmark")
# unless (open(LS, "./dry2 $times | tail -3 |"));
unless (open(LS, "echo $times |./dry2 |"));
@lsout = <LS>;
print "<PRE>\n";
foreach $name (@lsout) {
chomp($name);
print $name, "<br>\n";
}
print "</PRE>\n";
print end_html;
