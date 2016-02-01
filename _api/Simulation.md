---
title: Simulation
layout: api

---

### Public attributes

{: .table .table-striped .table-condensed}
| type   | name     |
|:-------|:---------|
| [WorkUnit]({{site.url}}/) | work_unit |
| std::string | platform |
| std::string | precision |
| int | deviceId |
| int | platformId |
| bool | verifyAccuracy |
| int | nan_check_freq |
| std::chrono::seconds | run_length |



### Public functions

{: .table .table-striped .table-condensed}
| type   | name     |
|:-------|:---------|
| None | Simulation() |
| map< string, string > | getPropertiesMap() const  |
| std::string | summary() const  |
| [SimulationResult]({{site.url}}/) | run(const Updater &update) const  |

