# Sets
* Bunch of elements/members 
* Represent using Capital letters

## Rules
* Member cannot be repeated
```
A = {1,2,2,3} 
```
* Order of member does not matter
```
{1,2,3} = {2,1,3}
```
## Notation
### Roster Notation
```
A = {1,2,3,4,5}
```
### Set-builder Notation
```
A = {x|x is integer between 1 and 5}
```
## Examples
* A is a set with members 1,2,3,4,5
```
A = {1,2,3,4,5}
B = {2,4,6,8}
```
* 3 is member of set A
```
3 Ⲉ A 
```
### Combining sets

* Intersection
```
A 𝉅 B = {2,4}
A 𝉅 B = {x|x ∈ A Λ x ∈ B}
```
* Union
```
A 𝈱 B = {1,2,3,4,5,6,8}
A 𝈱 B = {x|x ∈ A V x ∈ B}
```
* Difference (for understanding A − B)
```
A \ B = {x|x ∈ A Λ x ∉ B}
A \ B = {1,3,5}
```
* Symmetric Difference
```
A Δ B = {1,3,5,6,8}
A Δ B = {x|x ∈ A ⊕ x ∈ B}
A Δ B = A \ B 𝈱 B \ A
```
### Subsets
#### Trivial subsets
* Null(∅) set is subset of any set
* Every set is subset of its own
```
A = {1,2,3,4,5}
C = {1,3,5,7}
D = {1,2,3}

if
x ∈ D ⇒ x ∈ A
then
D ⊆ A
A ⊇ D

C ⊈ A
∅ ⊆ A
A ⊆ A
```
### Equality
```
if
A ⊆ F
F ⊆ A
then
A = F
```
### Universal Set
The set of everything we care about in the context of our problem.
```
U = {1,2,3,4,5,6,7,8,9,10}
```
### Complement
```
Aᶜ = U \ A
Aᶜ = {6,7,8,9,10}

(A 𝈱 B)ᶜ = Aᶜ 𝉅 Bᶜ
(A 𝉅 B)ᶜ = Aᶜ 𝈱 Bᶜ
```
### Special Sets
* Natural numbers
```
ℕ = {0, 1, 2, 3, ...}
ℕ* = ℕ ∖ {0} = {1, 2, 3, ...}
ℕᴋ = {0, 1, 2, 3, ..., k − 1}
```
* Integers
```
ℤ = {..., −3, −2, −1, 0, 1, 2, 3, ...}
ℤ* = ℤ ∖ {0} = {..., −3, −2, −1, 1, 2, 3, ...}
```
* Rational numbers
```
ℚ = {...,-1,-1/2,1,2/3,2,...}
```
* Irrational numbers
An irrational number is any real number that cannot be expressed as a ratio of integers.
```
π ≈ 3.14159265358... ≈ 22/7
e ≈ 2.71828182845...
√2 ≈ 1.41421356237...
```
* Real numbers
```
ℝ = ℚ (Rational numbers) 𝈱 Irrational numbers
```
* Complex numbers
```
ℂ = a + b √1
```
### Logical Operators
* Conjunction (And)
```
Λ
```
* Disjunction (Or)
```
V
```
* XOR
```
⊕
```

