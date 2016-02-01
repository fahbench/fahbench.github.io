---
title: CentralWidget
layout: api

---

### Public attributes

{: .table .table-striped .table-condensed}
| type   | name     |
|:-------|:---------|
| QLabel * | status_bar |
| QProgressBar * | progress_bar |
| QPushButton * | start_button |
| QPushButton * | cancel_button |
| [ResultsWidget]({{site.url}}/) | results_wid |



### Public functions

{: .table .table-striped .table-condensed}
| type   | name     |
|:-------|:---------|
| None | CentralWidget() |
| QSize | sizeHint() const  |
| void | configure_simulation(Simulation &sim) const  |

