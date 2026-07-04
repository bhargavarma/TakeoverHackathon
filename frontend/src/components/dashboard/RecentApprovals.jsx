export default function RecentApprovals(){

return(

<div className="rounded-3xl bg-white/5 border border-white/10 p-8">

<h2 className="text-2xl font-bold mb-8">

Pending Approvals

</h2>

<div className="space-y-5">

{["Milk","Coffee","Sugar"].map((item)=>(

<div
key={item}
className="rounded-2xl bg-white/5 p-5 flex justify-between">

<div>

<h3 className="font-semibold">

{item}

</h3>

<p className="text-gray-400">

Waiting Approval

</p>

</div>

<button className="rounded-xl bg-violet-600 px-5">

Review

</button>

</div>

))}

</div>

</div>

)

}