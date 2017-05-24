with import <nixpkgs> {};
let
  py = pkgs.python27Packages;
in

{ stdenv ? pkgs.stdenv }:

stdenv.mkDerivation {
  name = "brobot";
  version = "0.1.0.0";
  src = ./.;
  buildInputs = [ python
                  py.bitcoin-price-api
                  py.pep8
                  py.pyflakes
                  py.pylint
                  sqlite ];
}
