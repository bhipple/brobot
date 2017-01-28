with import <nixpkgs> {}; {
  pyEnv = stdenv.mkDerivation {
    name = "py";
    buildInputs = [ stdenv
                    python27Full
                    python27Packages.pyflakes
                    python27Packages.pep8
                    python27Packages.pylint
                    python27Packages.requests
                  ];
  };
}
