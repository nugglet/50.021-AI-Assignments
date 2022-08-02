Week 10 HW: Victoria Yong 1004455
# LP2 Output

## Output Summary
```
	(move tampines bedok)
	(pick bedok truck package1)
	(move bedok changi)
	(drop changi truck package1)
```

## Detailed Output
```
 (:action move
    :parameters (tampines bedok)
    :precondition
      (and
        (loc tampines)
        (loc bedok)
        (truck-at tampines)
      )
    :effect
      (and
        (truck-at bedok)
        (not
          (truck-at tampines)
        )
      )
  )

   (:action pick
    :parameters (bedok truck package1)
    :precondition
      (and
        (loc bedok)
        (truck truck)
        (package package1)
        (package-at package1 bedok)
        (truck-at bedok)
        (free truck)
      )
    :effect
      (and
        (not
          (package-at package1 bedok)
        )
        (not
          (free truck)
        )
        (carry package1 truck)
      )
  )

   (:action move
    :parameters (bedok changi)
    :precondition
      (and
        (loc bedok)
        (loc changi)
        (truck-at bedok)
      )
    :effect
      (and
        (truck-at changi)
        (not
          (truck-at bedok)
        )
      )
  )

   (:action drop
    :parameters (changi truck package1)
    :precondition
      (and
        (loc changi)
        (truck truck)
        (package package1)
        (carry package1 truck)
        (truck-at changi)
      )
    :effect
      (and
        (package-at package1 changi)
        (free truck)
        (not
          (carry package1 truck)
        )
      )
  )
```

# LP3 Output

## Output Summary 
```
  (move tampines bedok)
  (pick bedok truck package1)
  (move bedok changi)
  (drop changi truck package1)
  (pick changi truck package2)
  (move changi bedok)
  (drop bedok truck package2)
```

## Detailed Output
```
 (:action move
    :parameters (tampines bedok)
    :precondition
      (and
        (loc tampines)
        (loc bedok)
        (truck-at tampines)
      )
    :effect
      (and
        (truck-at bedok)
        (not
          (truck-at tampines)
        )
      )
  )

  (:action pick
    :parameters (bedok truck package1)
    :precondition
      (and
        (loc bedok)
        (truck truck)
        (package package1)
        (package-at package1 bedok)
        (truck-at bedok)
        (free truck)
      )
    :effect
      (and
        (not
          (package-at package1 bedok)
        )
        (not
          (free truck)
        )
        (carry package1 truck)
      )
  )
  
   (:action move
    :parameters (bedok changi)
    :precondition
      (and
        (loc bedok)
        (loc changi)
        (truck-at bedok)
      )
    :effect
      (and
        (truck-at changi)
        (not
          (truck-at bedok)
        )
      )
  )

  (:action drop
    :parameters (changi truck package1)
    :precondition
      (and
        (loc changi)
        (truck truck)
        (package package1)
        (carry package1 truck)
        (truck-at changi)
      )
    :effect
      (and
        (package-at package1 changi)
        (free truck)
        (not
          (carry package1 truck)
        )
      )
  )

   (:action pick
    :parameters (changi truck package2)
    :precondition
      (and
        (loc changi)
        (truck truck)
        (package package2)
        (package-at package2 changi)
        (truck-at changi)
        (free truck)
      )
    :effect
      (and
        (not
          (package-at package2 changi)
        )
        (not
          (free truck)
        )
        (carry package2 truck)
      )
  )

   (:action move
    :parameters (changi bedok)
    :precondition
      (and
        (loc changi)
        (loc bedok)
        (truck-at changi)
      )
    :effect
      (and
        (truck-at bedok)
        (not
          (truck-at changi)
        )
      )
  )

   (:action drop
    :parameters (bedok truck package2)
    :precondition
      (and
        (loc bedok)
        (truck truck)
        (package package2)
        (carry package2 truck)
        (truck-at bedok)
      )
    :effect
      (and
        (package-at package2 bedok)
        (free truck)
        (not
          (carry package2 truck)
        )
      )
  )
```