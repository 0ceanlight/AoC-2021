/forward/ { horiz += $2; vert += aim * $2 }
/down/ { aim += $2 }
/up/ { aim -= $2 }
END { print horiz * vert }
