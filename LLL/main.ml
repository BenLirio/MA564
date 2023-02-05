type expr =
  | Sum of int*int*expr
  | Mul of expr*expr
  | Z
  | Vec of int list
