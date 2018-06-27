<?php
$n = 100;
$data1 = array(32, 19, 10, 24, 15);
$data2 = array(28, 13, 18, 29, 12);

function calc_entropy($data, $n) {
    $h = 0;
    foreach ($data as $d) {
        $p = $d / $n;
        $h += - $p * log($p, 10);
    }
    return $h;
}
echo calc_entropy($data1, $n) . "\n";
echo calc_entropy($data2, $n) . "\n";
?>
