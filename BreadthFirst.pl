distance(1,2,782.62).
distance(2,1,782.62).
distance(1,8,869.63).
distance(8,1,869.63).
distance(1,6,1320).
distance(6,1,1320).
distance(2,6,1790).
distance(6,2,1790).
distance(10,6,680.19).
distance(6,10,680.19).
distance(7,10,847.04).
distance(10,7,847.04).
distance(7,5,1450).
distance(5,7,1450).
distance(10,4,1040).
distance(4,10,1040).
distance(4,3,501.52).
distance(3,4,501.52).
distance(5,4,656.86).
distance(4,5,656.86).
distance(9,3,590.89).
distance(3,9,590.89).
distance(8,9,1010).
distance(9,8,1010).

h1(1,1330).
h1(2,1460).
h1(3,1470).
h1(4,1150).
h1(5,1270).
h1(6,0).
h1(7,298.67).
h1(8,2090).
h1(9,2080).
h1(10,770.39).

h(Node,Cost):-h1(Node,Cost).
h(_,1).

routecost([X,Y],T):-distance(Y,X,T).
routecost([X,First|Rest],G):-routecost([First|Rest],Y1),distance(First,X,Y),G is Y1+Y.

bfs([[Target|Path]|_],Target,[Target|Path],0).
bfs([Path|Queue],Target,FinalPath,N) :-extend(Path,NewPaths),append(Queue,NewPaths,Queue1),sort1(Queue1,NewQueue), wrq(NewQueue),bfs(NewQueue,Target,FinalPath,M),N is M+1.

printroute([L]):-write(L),!.
printroute([L|Rest]):-printroute(Rest),write(" --> "),printroute([L]).

findroute(Start,Goal,Cost):-bfs([[Start]],Goal,N,P),printroute(N),routecost(N,Cost).

extend([Node|Path],NewPaths) :- findall([NewNode,Node|Path],(distance(Node,NewNode,_),\+ member(NewNode,Path)),NewPaths).

sort1(L,L2) :-swap1(L,L1), !,sort1(L1,L2).
sort1(L,L).

swap1([[X1|Y1],[X2|Y2]|T],[[X2|Y2],[X1|Y1]|T]) :-heuristic(X1,W1),heuristic(X2,W2),W1>W2.
swap1([X|T],[X|V]) :-swap1(T,V).

heuristic(Node, Cost) :-h(Node,Cost),number(Cost), !.
heuristic(Node, Cost) :-write('Incorrect heuristic functionh: '),write(h(Node, Cost)), nl,abort.

wrq(Q) :- length(Q,N).
