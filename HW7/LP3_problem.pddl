; Logistic Problem 3, Problem
(define (problem LP3)
   (:domain LP1)
   (:objects changi tampines bedok package1 package2 truck)
   (:init (loc tampines)
          (loc bedok)
          (loc changi)
          (truck truck)
          (package package1)
          (package package2)
          (truck-at tampines)
          (package-at package1 bedok)
          (package-at package2 changi)
          (free truck)
          )
         
   (:goal (and (package-at package1 changi) (package-at package2 bedok))))