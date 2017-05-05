#!/usr/bin/perl
print "Choose Operation \n1.Match\n2.Substitute\n3.transliterate\n";
$choice=<>;
print "\nENTER INPUT\n";
$string=<>;
if ($choice != 3)
{
print "Enter the regular expression\n";
$ex=<>;
chomp($ex);
chomp($string);
if($choice ==1)
	{
	print "MATCH OPERATOR\n";
	if($string =~ m/$ex/)
		{
		print "The regular expression is present\n";
		}
	else
		{
		print "The expression is no present\n";
		}
	}
elsif($choice == 2)
	{
	print "SUBSTITUTION OPERATOR\n";
	print "ENTER NEW WORD\n";
	$rp=<>;
	chomp($rp);
	if($string =~ s/\Q$ex/\Q$rp/)
		{
		print "THE SUBSTITUTED STRING is $string\n ";
		}
	else
		{
		print "THE REGULAR EXPRESSION DOES NOT EXIST\n";
		}
	}
}
elsif($choice == 3)
	{
	print "TRANSLITERATE OPERATOR\n";
	$string =~ tr[a-e][f-j];
	print "the transliterated string is    ",$string,"\n";
	}
else 
	{
	print "this operation does not exist\n";
	}

	
	


