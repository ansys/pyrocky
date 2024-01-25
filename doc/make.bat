@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=_build

REM TODO: these lines of code should be removed once the feature branch is merged
for /f %%i in ('pip freeze ^| findstr /c:"sphinx-autoapi @ git+https://github.com/ansys/sphinx-autoapi"') do set is_custom_sphinx_autoapi_installed=%%i
if NOT "%is_custom_sphinx_autoapi_installed%" == "sphinx-autoapi" (
	pip uninstall --yes sphinx-autoapi
	pip install "sphinx-autoapi @ git+https://github.com/ansys/sphinx-autoapi@feat/single-page-stable")
REM TODO: these lines of code should be removed once the feature branch is merged

if "%1" == "" goto help
if "%1" == "clean" goto clean
if "%1" == "pdf" goto pdf

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:clean
rmdir /s /q %BUILDDIR% > /NUL 2>&1
for /d /r %SOURCEDIR% %%d in (_autosummary) do @if exist "%%d" rmdir /s /q "%%d"
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%


:pdf
	%SPHINXBUILD% -M latex %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
	cd "%BUILDDIR%\latex"
	for %%f in (*.tex) do (
	pdflatex "%%f" --interaction=nonstopmode)
	if NOT EXIST pyrocky.pdf (

		Echo "no pdf generated!"
		exit /b 1)
	Echo "pdf generated!"

:end
popd
