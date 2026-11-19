# Asset audit — port/ch22-to-end

Source files: 9, port files: 23

## BGM (formula t{K-1})
- source play ids: 20 unique; expected tracks: [2, 3, 4, 6, 8, 12, 14, 17, 18, 19, 20, 21, 24, 25, 26, 27, 28, 29, 30, 31]
- port tracks: 20 unique
- missing tracks: none
- extra tracks (not from source): none

## Images
- source image ids: 109; map rows: 313; ids missing from map: []
- source ids not seen as id(K) placeholder in port: 5 (may be named directly) [2, 38, 58, 194, 1145]
- placeholders in port: 104 distinct; of them with filled filename: 35 (W6 risk)

## SE / movie / FX
- source BGM-stop events: 127; port stop music: 122
- source MOVIE calls: 2; port play sound: {}
- fx calls: {'fade_fx': 325, 'dissolve_fx': 600, 'flash_fx': 23, 'shake_fx': 104}

