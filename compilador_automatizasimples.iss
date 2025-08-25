; Script Inno Setup - Instalador para Automatiza Simples
; Autor: Bruno Jerônimo
; Versão: 1.0.0

[Setup]
AppName=Automatiza Simples
AppVersion=1.0.0
AppPublisher=Bruno Jerônimo
AppPublisherURL=https://www.linkedin.com/in/bruno-jeronimo/
DefaultDirName={userappdata}\Automatiza Simples
DefaultGroupName=Automatiza Simples
UninstallDisplayIcon={app}\main.exe
Compression=lzma
SolidCompression=yes
OutputDir=dist_instalador
OutputBaseFilename=AutomatizaSimples_Setup
SetupIconFile=assets\icone_ico.ico
WizardStyle=modern
PrivilegesRequired=lowest
; Sem precisar de administrador

[Languages]
Name: "portuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "Ícones adicionais:"; Flags: unchecked

[Files]
; Executável principal
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
; Pasta assets (ícones)
Source: "assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs ignoreversion

[Icons]
Name: "{group}\Automatiza Simples"; Filename: "{app}\main.exe"
Name: "{commondesktop}\Automatiza Simples"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\main.exe"; Description: "Executar Automatiza Simples"; Flags: nowait postinstall skipifsilent
