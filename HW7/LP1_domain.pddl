; Logistic Problem 1, Domain
; Assume truck can only carry 1 package at a time
(define (domain LP1)
	(:predicates 
			(loc ?l)
			(truck ?t)
			(package ?p)

			(truck-at ?l)
			(package-at ?p ?l)
			(free ?t)
			(carry ?p ?t)
	)

	(:action move
       :parameters  (?from ?to)
       :precondition (and  (loc ?from) (loc ?to) (truck-at ?from))
       :effect (and  (truck-at ?to)
		     		(not (truck-at ?from)))
	)

	(:action pick
       :parameters (?loc ?truck ?package)
       :precondition  (and  (loc ?loc) (truck ?truck) (package ?package)
			    		(package-at  ?package ?loc) (truck-at ?loc) (free ?truck))
       :effect (and (not (package-at ?package ?loc)) (not (free ?truck)) (carry ?package ?truck))
    )


   (:action drop
       :parameters  (?loc ?truck ?package)
       :precondition  (and  (loc ?loc) (truck ?truck) (package ?package)
       					(carry ?package ?truck) (truck-at ?loc))
       :effect (and (package-at ?package ?loc) (free ?truck) (not (carry ?package ?truck)))
    )
)
