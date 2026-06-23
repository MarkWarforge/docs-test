# Unity Project Folder Structure

> **Audience:** Everyone who creates or imports assets — artists, technical artists, engineers, designers.
>
> **Owners:** **Emman (Lead Artist)** owns all art-asset naming (materials, shaders, meshes, textures, VFX). **Amera (Tech Lead)** owns the engineering boundary (prefab names, ScriptableObject names, folder structure that Addressables depends on).
>
> **Status:** Living.

## Main Folder Structure

```text
Assets/
├── _Project/
│   ├── Core/
│   ├── Features/
│   ├── Shared/
│   ├── UI/
│   ├── Networking/
│   └── Bootstrap/
├── _WarforgeEngine/  
├── ThirdParty/
├── Plugins/
└── Editor/
```

### Key Points
Anything project related should be inside _Project folder making it clear that all scripts, files, etc. created for the project execution will be inside that folder.
Any third partner, plugin and editors we build should be outside the project folder.


## Bootstrap
Responsible for initialize global services, connect network, load first scene, setup our DI flow.

```text
Bootstrap/
├── GameBootstrap.cs
├── DependencyInstaller.cs
├── SceneLoader.cs
├── ServiceRegistry.cs
└── AppStateMachine.cs
```

## Core
Responsible for global systems

```text
Core/
├── Events/
│   ├── GameEventBus.cs
│   └── EventTypes.cs
├── State/
│   ├── GameState.cs
│   └── SessionState.cs
├── Time/
│   ├── GameTimeService.cs
│   └── EventTypes.cs
├── SaveSystem/
│   ├── SaveManager.cs
│   └── SaveData.cs
├── Utilities/
│   ├── Logger.cs
│   └── MathUtils.cs
└── Extensions/
```

## _Project folder structure
Everything should be organized by feature. Some of the possible features:
- Heroes
- Combat
- Alliance
- City
- WorldMap
- Economy
- Pets
- Artifacts
- Quests
- Behemoths

```text
Assets/
└── _Project/
    ├── Heroes/
    ├── Combat/
    ├── Alliance/
    ├── City/
    ├── Economy/
    ├── Pets/
    ├── Artifacts/
    ├── Quests/
    └── Behemoths/
        ├── Core/
        ├── Features/
        ├── Shared/
        ├── UI/
        ├── World/
        ├── Networking/
        └── Bootstrap/
```

Inside each feature we would have a structure of **DataProviders, Services, Controllers, Views, Model**

### Let’s see an example using Heroes 

```text
Assets/
└── _Project/
    └── Heroes/
        ├── DataProviders/
        ├── Services/
        ├── Controllers/
        ├── Views/
        └── Models/
```

## Art & Asset Folder Structure

Two zones, because shared and feature-specific assets organize differently:

```text
Assets/_Project/
  _Shared/
    Materials/
      Opaque_TrimSheets/    M_GEN_Metal_Trims …      (grouped by master shader)
      Opaque_Tileable/
      Transparent_Masked/
    Shaders/                SH_Opaque_TrimSheets …
  Buildings/
    Barracks/               PF_KL_Barracks_Lvl03, SK_, SO_KL_BarracksDefinition …
  Units/
  Factions/
    KnightsOfLight/         faction-exclusive art
  UI/  Environment/  Audio/  VFX/
```

Generic shared materials live in `_Shared`, **grouped by master shader** because that's the perf-relevant grouping. Feature-specific assets live with their feature. Third-party packages stay in `Plugins/` and are never renamed.
