from physics.box_collider import BoxCollider

b1 = BoxCollider(10, 10)
b2 = BoxCollider(12, 48)
b1.y = 100

print(b1.overlap(b2))