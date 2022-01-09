gnuplot -e '
set terminal eps;
set output "./extraction/results_'$1'.eps";
set datafile separator ",";
set style fill solid border lc rgb "black";
set boxwidth 1;
set yrange [0:];
set title  "'$1'";
set xtics font "Times New Roman,10";
plot "./extraction/results_'$1'.csv" using ($0*4+0):2 with boxes lw 2 lc rgb "light-cyan" title "Precision",
     "./extraction/results_'$1'.csv" using ($0*4+0):2:5 with yerrorbars title "",
     "./extraction/results_'$1'.csv" using ($0*4+1):3:xtic(1) with boxes lw 2 lc rgb "light-green" title "Recall",
     "./extraction/results_'$1'.csv" using ($0*4+1):3:6 with yerrorbars title "",
     "./extraction/results_'$1'.csv" using ($0*4+2):4 with boxes lw 2 lc rgb "light-pink"  title "F1",
     "./extraction/results_'$1'.csv" using ($0*4+2):4:7 with yerrorbars title "";
replot;
'