import {
ResponsiveContainer,
LineChart,
Line,
XAxis,
YAxis,
Tooltip,
} from "recharts";

const data=[

{day:"Mon",value:4000},

{day:"Tue",value:6500},

{day:"Wed",value:6000},

{day:"Thu",value:8200},

{day:"Fri",value:9000},

{day:"Sat",value:7600},

];

export default function RevenueChart(){

return(

<div className="rounded-3xl bg-white/5 border border-white/10 p-8 h-[420px]">

<h2 className="text-2xl font-bold mb-8">

Revenue Trend

</h2>

<ResponsiveContainer width="100%" height="90%">

<LineChart data={data}>

<XAxis dataKey="day"/>

<YAxis/>

<Tooltip/>

<Line
type="monotone"
dataKey="value"
stroke="#7c3aed"
strokeWidth={4}
/>

</LineChart>

</ResponsiveContainer>

</div>

)

}