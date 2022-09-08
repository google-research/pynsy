with import <nixpkgs> { };

let
  pythonPackages = python38Packages;
in pkgs.mkShell rec {
  venvDir = "./.venv38";
  buildInputs = [
    pythonPackages.python
    pythonPackages.venvShellHook
  ];

  LD_LIBRARY_PATH = "${stdenv.cc.cc.lib}/lib/";

  # Now we can execute any commands within the virtual environment.
  # This is optional and can be left out to run pip manually.
  postShellHook = ''
    pip install --upgrade pip
    pip install -r requirements.txt
  '';
}
