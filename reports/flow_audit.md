# Ren'Py flow audit — port/ch22-to-end

Files: 28, labels: 592, jumps: 754, calls: 7, menus: 115, returns: 28

## Broken jump/call targets: 0

## Unreachable labels in scope from chapter entry points: 103
ch23_1_scene_865, ch24_1_scene_901, ch25_2_scene_924, ch25_2_scene_925, ch25_2_scene_926, ch27_2_scene_992, sp90_scene_1536, sp90_scene_1537, sp90_scene_1538, sp90_scene_1539, sp90_scene_1540, sp90_scene_1541, sp90_scene_1542, sp90_scene_1543, sp90_scene_1544, sp90_scene_1545, sp90_scene_1546, sp90_scene_1547, sp90_scene_1548, sp90_scene_1549, sp90_scene_1550, sp90_scene_1551, sp90_scene_1552, sp90_scene_1562, sp90_scene_1563

## Cycles reachable from entries: 0

## Overlay K in scope: ['20', '21', '22', '23', '24', '25'] (duplicates: (none))

## Mainline chain
- ch22: files=5 labels=53 tail_jumps=['ch22_5_scene_1213', 'ch23', 'ch23']
- ch23: files=3 labels=48 tail_jumps=['ch23_3_scene_893', 'ch24', 'ch24']
- ch24: files=1 labels=10 tail_jumps=['ch24_1_scene_902', 'ch24_1_scene_902', 'ch25']
- ch25: files=4 labels=60 tail_jumps=['ch25_4_scene_1532', 'ch25_4_scene_1532', 'ch25_2_scene_927']
- ch26: files=6 labels=49 tail_jumps=['ch26_5_scene_1223', 'ch27', 'ch27']
- ch27: files=3 labels=30 tail_jumps=['ch27_3_scene_998', 'ch28', 'ch28']
- ch28: files=2 labels=12 tail_jumps=['ch28_1_scene_1007', 'ch28_2', 'attention']
