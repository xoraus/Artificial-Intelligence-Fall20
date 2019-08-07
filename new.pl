%connected(+Start, +Goal, -Weight)
connected(1,7,1).
connected(1,8,1).
connected(1,3,1).
connected(7,4,1).
connected(7,20,1).
connected(7,17,1).
connected(8,6,1).
connected(3,9,1).
connected(3,12,1).
connected(9,19,1).
connected(4,42,1).
connected(20,28,1).
connected(17,10,1).

connected2(X,Y,D) :- connected(X,Y,D).
connected2(X,Y,D) :- connected(Y,X,D).

next_node(Current, Next, Path) :-
    connected2(Current, Next, _),
    not(member(Next, Path)).

depth_first( Start, Goal, Path):-
    depth_first( Start, Goal, [Start], Path).


    consed(A,B,[B|A]).

bfs(Goal, [Visited|Rest], Path) :-                     % take one from front
    Visited = [Start|_],            
    Start \== Goal,
    findall(X,
        (connected2(X,Start,_),not(member(X,Visited))),
        [T|Extend]),
    maplist( consed(Visited), [T|Extend], VisitedExtended),      % make many
    append(Rest, VisitedExtended, UpdatedQueue),       % put them at the end
    bfs( Goal, UpdatedQueue, Path ).



 bfs(Goal, [[Goal|Visited]|_], Path):- 
    reverse([Goal|Visited], Path).


 breadth_first( Start, Goal, Path):- bfs( Goal, [[Start]], Path).