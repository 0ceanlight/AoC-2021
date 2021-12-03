BEGIN { 
FS = " " 
horiz = 0
vert = 0
}
/forward/ {horiz += $2}
/down/ {vert += $2}
/up/ {vert -= $2}
END {
print horiz
print vert
}
