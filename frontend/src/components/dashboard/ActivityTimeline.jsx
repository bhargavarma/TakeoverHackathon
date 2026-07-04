const data=[

["09:00","Inventory Reviewed"],

["09:01","Demand Forecast"],

["09:02","Supplier Selected"],

["09:03","Purchase Order Created"],

["09:04","Approval Email Sent"],

];

export default function ActivityTimeline(){

return(

<div className="rounded-3xl bg-white/5 border border-white/10 p-8">

<h2 className="text-2xl font-bold mb-8">

AI Timeline

</h2>

<div className="space-y-6">

{data.map((item,index)=>(

<div
key={index}
className="flex gap-5 items-center">

<div className="h-4 w-4 rounded-full bg-cyan-400"/>

<div>

<p className="text-sm text-gray-400">

{item[0]}

</p>

<h3>

{item[1]}

</h3>

</div>

</div>

))}

</div>

</div>

)

}