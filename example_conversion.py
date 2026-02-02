#!/usr/bin/env python3
"""
Simple example demonstrating SMILES to SAFE conversion
"""
import safe

def main():
    # Example molecules
    molecules = {
        "Ibuprofen": "CC(C)Cc1ccc(cc1)C(C)C(=O)O",
        "Aspirin": "CC(=O)Oc1ccccc1C(=O)O",
        "Caffeine": "CN1C=NC2=C1C(=O)N(C(=O)N2C)C",
        "Ethanol": "CCO",
    }

    print("SMILES to SAFE Conversion Examples")
    print("=" * 70)

    for name, smiles in molecules.items():
        print(f"\n{name}")
        print(f"  SMILES: {smiles}")

        try:
            # Encode to SAFE
            safe_str = safe.encode(smiles, slicer="brics")
            print(f"  SAFE:   {safe_str}")

            # Decode back
            decoded = safe.decode(safe_str, canonical=True)
            print(f"  Back:   {decoded}")

            # Verify round-trip
            import datamol as dm
            if dm.same_mol(smiles, decoded):
                print(f"  ✓ Round-trip successful")
            else:
                print(f"  ⚠ Round-trip changed molecule")

        except safe.SAFEFragmentationError:
            print(f"  ⚠ No fragmentable bonds (molecule too small)")
        except Exception as e:
            print(f"  ✗ Error: {e}")

    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
