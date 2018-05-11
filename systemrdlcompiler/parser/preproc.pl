use Safe;

my $perlfile = $ARGV[0];
my $code = do {
    local $/ = undef;
    open my $fhp, "<", $perlfile
        or die "could not open $perlfile: $!";
    <$fhp>;
};

open(local our $fh, '>', $ARGV[1]);
open(local our $fhl, '>', $ARGV[2]);
$compartment = new Safe;
$compartment->permit_only(':base_core', ':base_io', ':base_loop', 'rv2gv', 'padany');
$compartment->share('$fh', '$fhl');
$compartment->reval($code);
print $@;
close $fh;
