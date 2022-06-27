function GetCuurentDay(date) {
    let dayWeek = ''
    let day = date.getDate()
    let month = date.getMonth()
    let year = date.getFullYear()

    switch (date.getDay()) {
        case 1: dayWeek = 'Понедельник';
            break;
        case 2: dayWeek = 'Вторник';
            break;
        case 3: dayWeek = 'Среда';
            break;
        case 4: dayWeek = 'Четверг';
            break;
        case 5: dayWeek = 'Пятница';
            break;
        case 6: dayWeek = 'Суббота';
            break;
        case 0: dayWeek = 'Воскресенье';
            break;
      }
    
    currentDate = dayWeek + ', ' + day + '/' + month + '/' + year
    return currentDate
}


var vanillaCalendar = {
    month: document.querySelectorAll('[data-calendar-area="month"]')[0],
    next: document.querySelectorAll('[data-calendar-toggle="next"]')[0],
    previous: document.querySelectorAll('[data-calendar-toggle="previous"]')[0],
    label: document.querySelectorAll('[data-calendar-label="month"]')[0],
    activeDates: null,
    date: new Date,
    todaysDate: new Date,
    init: function(t) {
        this.options = t, this.date.setDate(1), this.createMonth(), this.createListeners()
    },
    createListeners: function() {
        var t = this;
        this.next.addEventListener("click", function() {
            t.clearCalendar();
            var e = t.date.getMonth() + 1;
            t.date.setMonth(e), t.createMonth()
        }), this.previous.addEventListener("click", function() {
            t.clearCalendar();
            var e = t.date.getMonth() - 1;
            t.date.setMonth(e), t.createMonth()
        })
    },

    

    createDay: function(t, e, a) {

    
        var n = document.createElement("div"),
            s = document.createElement("span");

        let dayWeel = ''

        s.innerHTML = t, 
        n.className = "vcal-date", 

    
        // n.setAttribute("data-calendar-date", this.date), 
        n.setAttribute("data-calendar-date", GetCuurentDay(this.date)), 
        
        1 === t && (n.style.marginLeft = 0 === e ? 6 * 14.28 + "%" : 14.28 * (e - 1) + "%"), 
        this.options.disablePastDays && this.date.getTime() <= this.todaysDate.getTime() - 1 ? n.classList.add("vcal-date--disabled") : (n.classList.add("vcal-date--active"), 
        n.setAttribute("data-calendar-status", "active")), 
        this.date.toString() === this.todaysDate.toString() && n.classList.add("vcal-date--today"), 
        n.appendChild(s), 
        this.month.appendChild(n)
    },
    dateClicked: function() {
        var t = this;
        this.activeDates = document.querySelectorAll('[data-calendar-status="active"]');
        for (var e = 0; e < this.activeDates.length; e++) this.activeDates[e].addEventListener("click", function(e) {
            document.querySelectorAll('[data-calendar-label="picked"]')[0].value = this.dataset.calendarDate, t.removeActiveClass(), this.classList.add("vcal-date--selected")
            // SPECIFIC PROJECT CODE START
            Upadateorder()
                document.getElementById('finish_order').scrollIntoView({ block: 'start',  behavior: 'smooth' }); 
                
            // END
        })
        
    },
    createMonth: function() {
        for (var t = this.date.getMonth(); this.date.getMonth() === t;) this.createDay(this.date.getDate(), this.date.getDay(), this.date.getFullYear()), this.date.setDate(this.date.getDate() + 1);
        this.date.setDate(1), this.date.setMonth(this.date.getMonth() - 1), this.label.innerHTML = this.monthsAsString(this.date.getMonth()) + " " + this.date.getFullYear(), this.dateClicked()
    },
    monthsAsString: function(t) {
        return ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"][t]
    },
    clearCalendar: function() {
        vanillaCalendar.month.innerHTML = ""
    },
    removeActiveClass: function() {
        for (var t = 0; t < this.activeDates.length; t++) this.activeDates[t].classList.remove("vcal-date--selected")
    }
};