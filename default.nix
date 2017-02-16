with import <nixpkgs> {};
with pkgs.python27Packages;

let
  bitcoin-price-api = buildPythonPackage rec {
    name = "bitcoin-price-api-${version}";
    version = "0.0.4";

    src = pkgs.fetchurl {
      url = "mirror://pypi/b/${name}.tar.gz";
      sha256 = "bc68076f9632aaa9a8009d916d67a709c1e045dd904cfc7a3e8be33960d32029";
    };

    buildInputs = with self; [ requests dateutil ];
    propagatedBuildInputs = with self; [ requests dateutil ];

    meta = {
      homepage = "http://github.com/dursk/bitcoin-price-api";
      description = "Price APIs for bitcoin exchanges";
      license = licenses.mit;
    };
  };
in

{ stdenv ? pkgs.stdenv }:

stdenv.mkDerivation {
  name = "brobot";
  version = "0.1.0.0";
  src = ./.;
  buildInputs = [ python
                  bitcoin-price-api
                  pep8
                  pyflakes
                  pylint
                  sqlite
                  sqlite3 ];
}
