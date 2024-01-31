class lib:
  def __init__(self) -> None:
    print("Paska")

  def kertotaulu(self) -> None:
    for x in range(1,11):
      for y in range(1,11):
        print(f"{x*y:4}", end="") #luo kertotaulun
      print()
