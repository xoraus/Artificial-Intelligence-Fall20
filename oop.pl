successor(a,b).
successor(b,a).
successor(b,c).
successor(a,d).
successor(b,d).
successor(d,b).
successor(d,e).
successor(e,d).


goalreached(e).


/* Problem-independent best-first search */
bestsearch(Start,Goalpathlist) :- cleandatabase,
  add_state(Start,[]), repeatifagenda,
  pick_best_state(State,Pathlist),
  add_successors(State,Pathlist), agenda(State,Goalpathlist,E),
  retract(agenda(State,Goalpathlist,E)), measurework.

pick_best_state(State,Pathlist) :-
  asserta(beststate(dummy,dummy,dummy)),
  agenda(S,SL,E), beststate(S2,SL2,E2), special_less_than(E,E2),
  retract(beststate(S2,SL2,E2)), asserta(beststate(S,SL,E)), fail.
pick_best_state(State,Pathlist) :- beststate(State,Pathlist,E),
  retract(beststate(State,Pathlist,E)), not(E=dummy), !.


add_successors(State,Pathlist) :- goalreached(State), !.
add_successors(State,Pathlist) :- successor(State,Newstate),
  add_state(Newstate,Pathlist), fail.
add_successors(State,Pathlist) :-
  retract(agenda(State,Pathlist,E)),
  asserta(usedstate(State)), fail.


add_state(Newstate,Pathlist) :- not(usedstate(Newstate)),
  not(agenda(Newstate,P,E)), eval(Newstate,Enew),
  asserta(agenda(Newstate,[Newstate|Pathlist],Enew)), !.
add_state(Newstate,Pathlist) :- not(eval(Newstate,Enew)),
  write('Warning: your evaluation function failed on state '),
  write(Newstate), nl, !.

/* Utility functions */
repeatifagenda.
repeatifagenda :- agenda(X,Y,Z), repeatifagenda.

special_less_than(X,dummy) :- !.
special_less_than(X,Y) :- X<Y.


cleandatabase :- checkabolish(agenda,3), checkabolish(usedstate,1),
  checkabolish(beststate,1), checkabolish(counter,1).


checkabolish(P,N) :- abolish(P,N), !.
checkabolish(P,N).


measurework :- countup(agenda(X,Y,Z),NA), countup(usedstate(S),NB),
  write(NA), write(' incompletely examined state(s) and '),
  write(NB),write(' examined state(s)'), !.


countup(P,N) :- asserta(counter(0)), call(P), counter(K),
  retract(counter(K)), K2 is K+1, asserta(counter(K2)), fail.
countup(P,N) :- counter(N), retract(counter(N)), !.



eval(S,0) :- goalreached(S).
eval(S,N) :- burial(c,S,N1), burial(e,S,N2), N is N1+N2+1.

burial(P,S,0) :- cleartop(P,S).
burial(P,S,N) :- member(on(X,P,B),S), burial(X,S,N2), N is N2+1.

