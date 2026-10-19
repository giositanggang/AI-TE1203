class TemperatureAgent:
    def __init__(self, temperature):
        self.temperature = temperature

    def decide(self):
        if self.temperature >= 30:
            return "Kipas ON"
        else:
            return "Kipas OFF"


class LightAgent:
    def __init__(self, light_level):
        self.light_level = light_level

    def decide(self):
        if self.light_level < 40:
            return "Lampu ON"
        else:
            return "Lampu OFF"


class RoomAgent:
    def __init__(self, people_present):
        self.people_present = people_present

    def decide(self):
        if self.people_present:
            return "Ruangan digunakan"
        else:
            return "Ruangan kosong"


class MultiAgentSystem:
    def run(self):
        print("=== MULTI-AGENT SYSTEM ===")
        print("Sistem Pengelolaan Ruangan Kampus\n")

        try:
            temperature = float(
                input("Masukkan suhu ruangan (C): ")
            )
            light_level = float(
                input("Masukkan intensitas cahaya (0-100): ")
            )
            people = input(
                "Apakah ada orang di ruangan? (ya/tidak): "
            ).strip().lower()

            if not 0 <= light_level <= 100:
                print("Intensitas cahaya harus 0-100.")
                return

            if people not in ("ya", "tidak"):
                print("Input keberadaan orang tidak valid.")
                return

            # Membuat tiga agent
            temperature_agent = TemperatureAgent(temperature)
            light_agent = LightAgent(light_level)
            room_agent = RoomAgent(people == "ya")

            # Setiap agent mengambil keputusan
            fan = temperature_agent.decide()
            light = light_agent.decide()
            room = room_agent.decide()

            # Menampilkan hasil kerja sama agent
            print("\n=== HASIL KEPUTUSAN AGENT ===")
            print("Agent Suhu   :", fan)
            print("Agent Cahaya :", light)
            print("Agent Ruangan:", room)

            # Sistem menggabungkan keputusan para agent
            if people == "tidak":
                light = "Lampu OFF"
                fan = "Kipas OFF"

            print("\n=== KEPUTUSAN AKHIR SISTEM ===")
            print("Status Lampu :", light)
            print("Status Kipas :", fan)
            print("Status Ruangan:", room)

        except ValueError:
            print("Input suhu dan cahaya harus berupa angka.")


if __name__ == "__main__":
    system = MultiAgentSystem()
    system.run()
