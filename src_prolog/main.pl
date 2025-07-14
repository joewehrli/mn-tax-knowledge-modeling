:- use_module(facts/parcels).
:- use_module(facts/ownership).
:- use_module(facts/land_use).
:- use_module(facts/programs).
:- use_module(facts/declarations).
:- use_module(facts/valuation).
:- use_module(rules/residential).
:- use_module(utils/output).

classify_parcel(ParcID) :-
    classify_residential(ParcID, Class),
    format('Parcel ~w classified as: ~w~n', [ParcID, Class]).
