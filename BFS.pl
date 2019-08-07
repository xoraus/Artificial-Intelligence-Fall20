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





state_record(State, Parent, [State, Parent]).

go(Start, Goal) :- 
    empty_queue(Empty_open),
    state_record(Start, nil, State),
    add_to_queue(State, Empty_open, Open),
    empty_set(Closed),
    path(Open, Closed, Goal).

path(Open,_,_) :- empty_queue(Open),
                  write('graph searched, no solution found').
    
path(Open, Closed, Goal) :- 
    remove_from_queue(Next_record, Open, _),
    state_record(State, _, Next_record),
    State = Goal,
    write('Solution path is: '), nl,
    printsolution(Next_record, Closed).
    
path(Open, Closed, Goal) :- 
    remove_from_queue(Next_record, Open, Rest_of_open),
    (bagof(Child, moves(Next_record, Open, Closed, Child), Children);Children = []),
    add_list_to_queue(Children, Rest_of_open, New_open), 
    add_to_set(Next_record, Closed, New_closed),
    path(New_open, New_closed, Goal),!.

moves(State_record, Open, Closed, Child_record) :-
    state_record(State, _, State_record),
    mov(State, Next),
    % not (unsafe(Next)),
    state_record(Next, _, Test),
    not(member_queue(Test, Open)),
    not(member_set(Test, Closed)),
    state_record(Next, State, Child_record).

printsolution(State_record, _):- 
    state_record(State,nil, State_record),
    write(State), nl.
printsolution(State_record, Closed) :-
    state_record(State, Parent, State_record),
    state_record(Parent, _, Parent_record),
    member(Parent_record, Closed),
    printsolution(Parent_record, Closed),
    write(State), nl.
        
add_list_to_queue([], Queue, Queue).
add_list_to_queue([H|T], Queue, New_queue) :-
    add_to_queue(H, Queue, Temp_queue),
    add_list_to_queue(T, Temp_queue, New_queue).