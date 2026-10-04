#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cay Bardagi Diplomatik Protokolu.

Son yudum krizini tutanak altina alir. Cam kirmaz, sadece karar verir.
Calistirmak icin: python protokol.py
"""

from __future__ import annotations

import argparse
import random
import sys


TARAFLAR = (
    "ince belli bardak",
    "komsu bardak",
    "tabak (gozlemci)",
    "seker kupu (erime hakkini kullanir)",
    "cay kasigi (veto yetkisi supheli)",
)

KARARLAR = (
    "son yudum ev sahibine birakilir, misafir kaş kaldirir",
    "son yudum paylasilamaz, tutanakta 'buharlasti' yazilir",
    "kriz ertelenir, bir cay daha istenir, bu da krizdir",
    "tabak arabulucu olur, kimse ciddiye almaz, cozum olur",
    "kasik masaya vurur, oturum dagilir, cay sogur",
)


def sicaklik_yorumu(sicaklik: int) -> str:
    if sicaklik >= 90:
        return "dil politikasi devreye girer: kimse icmez, herkes konusur"
    if sicaklik >= 70:
        return "ideal diplomasi araligi, yudumlar kisa ve nazik"
    if sicaklik >= 45:
        return "ilik, gerilim dusuk, kararlar sulandirilmis"
    return "sogumus cay, protokol maddesi 4 ihlali, tutanak kirmizi"


def oturum(tur: int, sicaklik: int, tohum: int | None) -> int:
    rng = random.Random(tohum)
    print("=" * 52)
    print(" CAY BARDAGI DISISLERI BAKANLIGI")
    print(" oturum no: CB-{}-".format(sicaklik) + f"{tur:02d}")
    print("=" * 52)
    print(sicaklik_yorumu(sicaklik))
    print()

    puan = {taraf: 0 for taraf in TARAFLAR if "gozlemci" not in taraf}
    for adim in range(1, tur + 1):
        taraf = rng.choice(list(puan))
        hamle = rng.choice(
            (
                "yudum hakki talep eder",
                "tabagi nota yerine kullanir",
                "seker politikasini elestirir",
                "susturucu buhar yayinlar",
                "bir cay daha diye ara seçim ister",
            )
        )
        puan[taraf] += 1
        print(f"[{adim}] {taraf} {hamle}. skor={puan[taraf]}")

    kazanan = max(puan, key=puan.get)
    karar = rng.choice(KARARLAR)
    print()
    print(f"sozcu: {kazanan}")
    print(f"karar: {karar}")
    print(f"sicaklik tutanagi: {sicaklik} C")
    print("oturum kapandi. bardak sapasağlam, ciddiyet kirik.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Ince belli bardaklar arasinda son yudum protokolu"
    )
    parser.add_argument("--tur", type=int, default=4, help="oturum turu")
    parser.add_argument("--sicaklik", type=int, default=82, help="cay sicakligi")
    parser.add_argument("--tohum", type=int, default=None, help="tekrar edilebilir kriz")
    args = parser.parse_args(argv)
    if args.tur < 1:
        print("tur en az 1 olur, bos bardak oturum acamaz", file=sys.stderr)
        return 2
    return oturum(args.tur, args.sicaklik, args.tohum)


if __name__ == "__main__":
    raise SystemExit(main())
