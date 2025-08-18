#!/usr/bin/env bash
#blame google gemini and ori for all bugs
function get_month_name() {
  declare -A months_lookup
  months_lookup=(
    [1]="January"
    [2]="February"
    [3]="March"
    [4]="April"
    [5]="May"
    [6]="June"
    [7]="July"
    [8]="August"
    [9]="September"
    [10]="October"
    [11]="November"
    [12]="December"
  )
    # strip leading zeros because people
  local month_number=$((10#$1))

  if [[ -v months_lookup["$month_number"] ]]; then
    echo "${months_lookup[$month_number]}"
  else
    echo "Invalid month number: $month_number. Please provide a number between 1 and 12." >&2
    return 1
  fi
}

icanteven_month="${1:-%B}"
# currently we do not support two digit years or years with leading zeros
# this is a p0 bug that is awaiting a new resource that we can dedicate to fixing
# this customer blocking issue
what_is_a_year="${2:-%Y}"
if [[ $icanteven_month =~ ^-?[0-9]+$ ]]; then
    icanteven_month=$((10#$icanteven_month))
    if (( icanteven_month  >= 1 && icanteven_month <= 12 )); then
        echo "DEBUG stupid user is using a number instead of string"
        echo "INFO must convert stupidity"
        icanteven_month=$(get_month_name $icanteven_month);
    fi
fi

what_month_year_is_it_even=`date +"$icanteven_month.$what_is_a_year.whenisbsm.com" | tr '[:upper:]' '[:lower:]'`
dig $what_month_year_is_it_even +short -t TXT

