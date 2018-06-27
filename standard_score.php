<?php
$n = 100;
$data = array(28, 13, 18, 29, 12);

function standard_score($data, $n) {
    $mean = 0;
    $dev = 0;
    foreach ($data as $d) {
        $mean += $d;
        $dev += $d * $d;
    }
    $mean /= $n;
    $dev = $dev / $n - $mean * $mean;

    $std_score = array();
    $dev_score = array();
    foreach ($data as $d) {
        $z = ($d - $mean) / $dev;
        $std_score[] = $z;
        $dev_score[] = 10 * $z + 50;
    }
    print_r($std_score);
    print_r($dev_score);
}
echo standard_score($data, $n) . "\n";
?>
