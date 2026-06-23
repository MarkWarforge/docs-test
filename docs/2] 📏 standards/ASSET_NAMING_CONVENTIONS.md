# Asset Naming & Folder Conventions

> **Audience:** Everyone who creates or imports assets — artists, technical artists, engineers, designers.
>
> **Owners:** **Emman (Lead Artist)** owns all art-asset naming (materials, shaders, meshes, textures, VFX). **Amera (Tech Lead)** owns the engineering boundary (prefab names, ScriptableObject names, folder structure that Addressables depends on).
>
> **Status:** Living.

## Golden rules

1. **No spaces, no special characters — including slashes.** `PascalCase` only. (See the two violations to fix in Emman's current list, below.)
2. **No version words.** No `_final`, `_v2`, `_FIXED`. Source control is your history.
3. **Prefix = type. Owner token = who it belongs to. Folder = where it's grouped.**
4. **Numbers zero-padded** to the expected max: `Lvl03`.
5. **Match an existing sibling exactly when unsure.**

## Naming pattern

```
<Prefix>_<Owner>_<Descriptor>[_<Variant>]
```

- **Prefix** = asset type (`M_`, `SH_`, `PF_`, `SK_`, …)
- **Owner** = `GEN` (generic, used by every faction) **or** a faction code (`KL`, `SM`, `FA`, `BT`)

## Materials & shaders

- **`SH_`** = Shader Graph (the master). Controls every material built on it.
- **`M_`** = Material (an instance of a master shader; edit it without touching siblings).
- Materials are grouped under the master shader they derive from:

| `SH_Opaque_TrimSheets` | `SH_Opaque_Tileable` | `SH_Transparent_Masked` |
|---|---|---|
| `M_GEN_Metal_Trims` | `M_GEN_Soil` | `M_GEN_Grass` |
| `M_GEN_Planks_Trims` | `M_GEN_Cobblestones` | `M_GEN_Leaves` |
| `M_GEN_Wood_Trims` | `M_GEN_Bricks` | `M_GEN_Bushes` |
| `M_GEN_Stone_Trims` | `M_GEN_Grasslands` | *(only when necessary)* |
| `M_GEN_Fabric_Trims` | `M_GEN_Sand` | |
| `M_GEN_FabricElegant_Trims` | `M_GEN_Fabric` | |
| `M_GEN_Crystals`, `M_GEN_Gems` | `M_GEN_Metal` | |
| `M_GEN_Glass` | `M_GEN_Mortar` | |
| `M_GEN_BonesHorns` | `M_GEN_Wood` | |

## Faction code table

| Code | Faction |
|------|---------|
| `GEN` | Generic / universal |
| `KL` | Knights of Light |
| `SM` | Storm Mages |
| `FA` | Forest Archers |
| `BT` | Barbarian Tribes |

Adding a faction = adding a row here first, before any asset uses the new code.

## Prefix table

| Type | Prefix | Type | Prefix |
|------|--------|------|--------|
| Material | `M_` ✅ | Shader Graph | `SH_` ✅ |
| Prefab | `PF_` | Static mesh | `SM_` |
| Skinned mesh | `SK_` | Texture | `T_` |
| Sprite | `SPR_` | Animation clip | `A_` |
| Animator controller | `AC_` | ScriptableObject | `SO_` |
| Scene | `SCN_` | VFX / particle | `FX_` |
| Audio – SFX | `SFX_` | Audio – music | `MX_` |
| UI element | `UI_` | | |

### Texture suffixes
`_BC` base color · `_N` normal · `_ORM` occlusion/roughness/metallic · `_M` mask · `_E` emissive.

## The engineering boundary

These names are referenced by code or load systems — renaming them silently breaks the game. Changes here go through Amera, not just art:

- **Prefab names** loaded by Addressables

- **ScriptableObject names/paths** referenced as config

- **Addressables group names**, which should mirror the folder zones above


## Validator

This doc is the spec; enforcement is a Unity **editor validation tool** (menu item or pre-commit hook) that flags violations. Until it exists, names will drift. Budget a day to build it.
