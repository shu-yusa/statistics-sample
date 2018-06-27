<?php
$n = 10;
$data_A = array(0, 3, 3, 5, 5, 5, 5, 7, 7, 10);
$data_B = array(0, 1, 2, 3, 5, 5, 7, 8, 9, 10);
$data_C = array(3, 4, 4, 5, 5, 5, 5, 6, 6, 7);

calc_gini($data_A, $n);
calc_gini($data_B, $n);
calc_gini($data_C, $n);

function calc_gini($data, $n) {
    $mean = 0;
    $mean_diff = 0;
    $gini_coef = 0;
    foreach($data as $d) {
        $mean += $d;
        foreach($data as $d2) {
            $mean_diff += abs($d - $d2);
        }
    }
    $mean /= $n;
    $mean_diff /= $n * $n;
    $gini_coef = $mean_diff / (2 * $mean);
    echo "mean : {$mean}\n";
    echo "mean difference : {$mean_diff}\n";
    echo "gini coefficient: {$gini_coef}\n\n";
}
