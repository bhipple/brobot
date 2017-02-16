with import <nixpkgs> {};

let
  bitcoin-price-api = pkgs.python27Packages.buildPythonPackage rec {
    name = "bitcoin-price-api-${version}";
    version = "0.0.4";

    src = pkgs.fetchurl {
      url = "mirror://pypi/b/${name}.tar.gz";
      sha256 = "bc68076f9632aaa9a8009d916d67a709c1e045dd904cfc7a3e8be33960d32029";
    };

    buildInputs = with self; with pkgs.python27Packages; [ requests dateutil ];
    propagatedBuildInputs = with self; with pkgs.python27Packages; [ requests dateutil ];

    meta = {
      homepage = "http://github.com/dursk/bitcoin-price-api";
      description = "Price APIs for bitcoin exchanges";
      license = licenses.mit;
    };
  };
in

# This works, but we can't add non-python packages like the system sqlite to it.
(pkgs.python27.withPackages (ps: [ps.pyflakes ps.pep8 ps.pylint ps.requests bitcoin-price-api])).env
