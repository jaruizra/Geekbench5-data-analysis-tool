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
        print("--- device hardware ---")
        print("CPU name =", self.cpu)
        print("CPU cores =", self.cores)
        print("GPU name =", self.gpu)
        print("Device RAM =", self.ram)
        print("-----------------------")

    def harware_description2(self, d):
        print("--- devices hardware ---")
        print("CPU 1 name =", self.cpu, " --- CPU 2 =", d.cpu)
        print("CPU 1 cores =", self.cores, " --- CPU 2 =", d.cores)
        print("GPU 1 name =", self.gpu, " --- GPU 2 =", d.gpu)
        print("Device 1 RAM =", self.ram, " --- Device 2 =", d.ram)
        print("------------------------")

    def main_c_data(self):
        print("--- cpu performance ---")
        print("Max freq =", max(self.frequency))
        print("Min freq =", min(self.frequency))
        print("Average freq =", sum(self.frequency)/len(self.frequency))
        print("Test frequencies =", self.frequency)
        print("-----------------------")

    def main_c_data2(self, d):
        print("--- cpu performance ---")
        print("Average 1 freq =", sum(self.frequency)/len(self.frequency), " --- Average 2 =", sum(d.frequency)/len(d.frequency))
        print("Max 1 freq =", max(self.frequency), " --- Max 2 =", max(d.frequency))
        print("Min 1 freq =", min(self.frequency), " --- Min 2 =", min(d.frequency))
        print("Test 1 frequencies =", self.frequency)
        print("Test 2 frequencies =", d.frequency)

        print("-----------------------")

    def results(self):
        print("--- Device Scores ---")
        print("Device single core =", self.s_score)
        print("Device multi core =", self.m_score)
        print("---------------------")

    def results2(self, d2):
        print("--- Devices Scores ---")
        print("Test 1 single core =", self.s_score, " --- Test 2 =", self.s_score)
        print("Test 1 multi core =", self.m_score, " --- Test 2 =  ", d2.m_score)
        print("----------------------")

    def print_compare(self, d2):
        print("")
        print("-----------------------------------------------------------------------")
        print("")
        print("Device test 1 =", self.model, "   Date =", d2.date)
        print("Device test 2 =", d2.model, "   Date =", d2.date)
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
        print("Device name =", self.model, "   Date =", self.date)
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
