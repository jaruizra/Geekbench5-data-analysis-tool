
class tests:
    def __init__(self, test):
        d = test
        d_m = d["metrics"]
        self.model = d_m[4 - 1]["value"]
        self.date = d["date"][0:10]
        self.frequency = d["processor_frequency"]["frequencies"]
        self.geek_version = d["version"]
        self.op_version = d_m[3 - 1]["value"]
        self.cpu = d_m[9 - 1]["value"]
        self.cores = d_m[11 - 1]["value"]
        self.ram = d_m[15 - 1]["value"]
        self.gpu = d_m[17 - 1]["value"]
        d_s = d["sections"]
        self.s_score = d_s[1 - 1]["score"]
        self.m_score = d_s[2 - 1]["score"]

    def harware_description(self):
        print("--- cpu data ---")
        print("CPU name =", self.cpu)
        print("CPU cores =", self.cores)
        print("GPU name =", self.gpu)
        print("Device RAM =", self.ram)
        print("----------------")

    def harware_description2(self, d):
        print("--- cpu data ---")
        print("CPU 1 name =", self.cpu, " --- CPU 2 =", d.cpu)
        print("CPU 1 cores =", self.cores, " --- CPU 2 =", d.cores)
        print("GPU 1 name =", self.gpu, " --- GPU 2 =", d.gpu)
        print("Device 1 RAM =", self.ram, " --- Device 2 =", d.ram)
        print("----------------")

    def main_c_data(self):
        print("--- cpu data ---")
        print("test frequencies =", self.frequency)
        print("max freq", max(self.frequency))
        print("min freq", min(self.frequency))
        print("average freq", sum(self.frequency)/len(self.frequency))
        print("----------------")

    def main_c_data2(self, d):
        print("--- cpu data ---")
        print("Device 1 frequencies =", self.frequency)
        print("Device 2 frequencies =", d.frequency)

        print("max 1 freq", max(self.frequency))
        print("max 2 freq", max(d.frequency))

        print("min 1 freq", min(self.frequency))
        print("min 2 freq", min(d.frequency))

        print("average 1 freq", sum(self.frequency)/len(self.frequency))
        print("average 2 freq", sum(d.frequency)/len(d.frequency))

        print("----------------")

    def results(self):
        print("--- results ---")
        print("Device single core =", self.s_score)
        print("Device multi core =", self.m_score)
        print("----------------")

    def results2(self, d2):
        print("--- results ---")
        print("Device 1 single core =", self.s_score, " --- Device 2 =", self.s_score)
        print("Device 1 multi core =", self.m_score, " --- Device 2 =  ", d2.m_score)
        print("----------------")

    def print_compare(self, d2):
        print("")
        print("-----------------------------------------------------------------------")
        print("")
        print("Model ID 1=", self.model, "   Date =", d2.date)
        print("Model ID 2=", d2.model, "   Date =", d2.date)
        print("")
        print(" --- BENCHMARK RESULTS --- ")
        self.results2(d2)
        print("")
        self.harware_description2(d2)
        print("")
        self.main_c_data2(d2)
        print("")
        print("-----------------------------------------------------------------------")
        print("")

    def print_important_analysis(self):
        print("")
        print("-----------------------------------------------------------------------")
        print("")
        print("Model ID =", self.model, "   Date =", self.date)
        print("")
        print(" --- BENCHMARK RESULTS --- ")
        self.results()
        print("")
        self.harware_description()
        print("")
        self.main_c_data()
        print("")
        print("-----------------------------------------------------------------------")
        print("")
