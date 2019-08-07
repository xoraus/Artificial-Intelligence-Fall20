member(X,[X|T]).
member(X,[H|T]) :- member(X,T).


conc([],A,A).
conc([X|L1], L2, [X|L3]):-conc(L1,L2,L3).



add(X,L,[X|L]).
addlast(X,[],[X]).

addlast(X,[H|T],[H|Z]) :- addlast(X,T,Z).



del([_|T], T).
delpop(X,[X|T],T).
delpop(X,[Y|T],[Y|T1]) :- delpop(X,T,T1).

delend([_],[]).
delend([H|T],[H|R]) :- delend(T,R).


sublist(S,L) :- conc(L1,L2,L),conc(S,L3,L2).

max([],A,A).
max([H|T], A, M) :- H > A, max(T,H,M).
max([H|T], A, M) :- =< A, max(T,A,M).
maximum([H|T], M) :- max(T,H,M).

list_sum([],0).
list_sum([Head|Tail], TotalSum):- list_sum(Tail, Sum1), TotalSum is Head+Sum1.


ordered( []) .
ordered( [_]     ) .
ordered( [X,Y|Z] ) :- X =< Y , ordered( [Y|Z] ) .

reverse([],Z,Z).
reverse([H|T],Z,Acc) :- reverse(T,Z,[H|Acc]).


secondLargest(List,X):- msort(List,SortedList),reverse(SortedList,[_|[X|_]]).