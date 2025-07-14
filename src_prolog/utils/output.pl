:- module(output, [pretty_classification/1]).

pretty_classification(ParcID) :-
    main:classify_parcel(ParcID).
