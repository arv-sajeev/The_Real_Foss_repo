#!/usr/bin/perl
$var = <<EOF;
$a = 100;
shshshhhshshsh $a
EOF
print "$var\n";
$end = <<'EOF';
shhshs $a
EOF
print "$end\n";
$str = "Welcome to tutorials point\nhope you have a good day";
$str1 = 'Welcome to tutorials point\nhope you have a good day';
$str = "\UWelcome to tutorials point\nhope you have a good day";
print "$str\n";
print "$str1\n";
@ages = (25,30,40);
print "\n$ages[0]\n$ages[1]\n$ages[2]\n";




$con = "hello"."world";
print "\n$con\n";
$con = "helo"*5;
print "\n$con\n";
print <<EOF;
This is a 
Multi
line string
EOF
print "file name  "._FILE_."\n";

