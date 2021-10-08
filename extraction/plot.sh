gnuplot -e '
set terminal png;
set output "./extraction/results.png";
set datafile separator ",";
set style fill solid border lc rgb "black";
set boxwidth 1;
set yrange [0:];
plot "./extraction/results.csv" using ($0*4+0):2 with boxes lw 2 lc rgb "light-cyan"  title "Precision",
     "./extraction/results.csv" using ($0*4+1):3:xtic(1) with boxes lw 2 lc rgb "light-green" title "Recall",
     "./extraction/results.csv" using ($0*4+2):4    with boxes lw 2 lc rgb "light-pink"  title "F1";
replot;
'